from mkdocs_chessboard_plugin.plugin import ChessboardPlugin

def test_on_page_markdown__valid_fen__renders_correct_html():
    # given
    plugin = ChessboardPlugin()
    sample_html = '''
<h1 id="rook-endgames">Rook endgames<a class="headerlink" href="#rook-endgames" title="Permanent link">&para;</a></h1>
<p>This section will cover rook endgames.</p>
<h2 id="rook-pawn-vs-rook">Rook + Pawn vs Rook<a class="headerlink" href="#rook-pawn-vs-rook" title="Permanent link">&para;</a></h2>
<p>One of the most common endgames is the rook and pawn vs rook endgame.
Typically, the side controlling the promotion square will decide the outcome of the game but it requires precise play to convert the advantage or hold the draw.</p>
<p>Here are some key positions to practice:</p>
<h3 id="philidor-position">Philidor Position<a class="headerlink" href="#philidor-position" title="Permanent link">&para;</a></h3>
<p>The Philidor position is a fundamental position in rook endgames where the defending side can hold a draw with accurate play. The key is to prevent the attacking king from entering the 7th rank.</p>
<div class="codehilite"><pre><span></span><code>[FEN 8/8/8/8/1kp5/8/7r/2K3R1 w - - 0 1]
</code></pre></div>
    '''

    # when
    output = plugin.on_page_content(sample_html)

    # then
    assert '<div class="chessboard"' in output
    assert 'var board = Chessboard' in output
    assert 'position: \'8/8/8/8/1kp5/8/7r/2K3R1 w - - 0 1\'' in output
    assert '<link rel="stylesheet" href="https://unpkg.com/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">' in output
    assert '<script src="https://unpkg.com/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>' in output