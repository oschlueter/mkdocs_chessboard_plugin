import re

from mkdocs.plugins import BasePlugin


class ChessboardPlugin(BasePlugin):

    def send_post_requests(self):
        return '''
        
<script>
    function sendPostRequest(level, clockLimit, clockIncrement, days, color, variant, fen) {
        const url = 'https://lichess.org/api/challenge/ai';
        const data = {
            level: level,
            clock: {
                limit: clockLimit,
                increment: clockIncrement
            },
            days: days,
            color: color,
            variant: variant,
            fen: fen
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            const challengeUrl = `https://lichess.org/${data.id}`;
            navigator.clipboard.writeText(challengeUrl).then(() => {
                console.log('Challenge URL copied to clipboard:', challengeUrl);
            }).catch(err => {
                console.error('Failed to copy URL to clipboard:', err);
            });
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
</script>
        '''


    def on_page_content(self, html, **kwargs):
        # Regular expression to find code blocks starting with ```FEN
        # fen_pattern = re.compile(r'<pre><span></span><code>\[FEN\s+([^<]+)\]</code></pre>', re.MULTILINE)
        fen_pattern = re.compile('<pre><span><\/span><code>\[FEN ([a-zA-Z0-9\/ -]+)]\s+<\/code><\/pre>', re.MULTILINE)
        def replace_fen(match):
            fen = match.group(1).strip()
            player = 'white' if fen.split(' ')[1] == 'w' else 'black'

            return f'''
                    <div class="chessboard" id="board-{fen.replace(' ', '_').replace('/', '_')}"></div>
                    <script>
                        var board = Chessboard('board-{fen.replace(' ', '_').replace('/', '_')}', {{
                            position: '{fen}',
                            orientation: '{player}',
                            pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{'{piece}.png'}'
                        }});
                    </script>
                    
                    <a href="#" class="post-link" onclick="sendPostRequest('{fen}', 7, '{player}'); return false;">Play against Stockfish level 7.</a>
                    <br>
                    <a href="#" class="post-link" onclick="sendPostRequest('{fen}', 8, '{player}'); return false;">Play against Stockfish level 8.</a>
                    '''

        # Replace all FEN code blocks in the HTML
        new_html = fen_pattern.sub(replace_fen, html)

        # Add the necessary CSS and JS for chessboard.js
        new_html = f'''
                {self.send_post_requests()} 
                <link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css" integrity="sha384-q94+BZtLrkL1/ohfjR8c6L+A6qzNH9R2hBLwyoAfu3i/WCvQjzL2RQJ3uNHDISdU" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
                <script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js" integrity="sha384-8Vi8VHwn3vjQ9eUHUxex3JSN/NFqUg3QbPyX8kWyb93+8AC/pPWTzj+nHtbC5bxD" crossorigin="anonymous"></script>

                ''' + new_html

        return new_html