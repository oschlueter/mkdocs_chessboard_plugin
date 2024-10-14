from mkdocs_chessboard_plugin.plugin import ChessboardPlugin

def test_on_page_markdown__valid_fen__renders_correct_html():
    # given
    plugin = ChessboardPlugin()
    sample_markdown = '''
    # Sample Document

    ```FEN
    rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    ```

    Some more text.
    '''

    # when
    output = plugin.on_page_markdown(sample_markdown)

    # then
    assert '<div class="chessboard"' in output
    assert 'var board = Chessboard' in output
    assert 'position: \'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1\'' in output
    assert '<link rel="stylesheet" href="https://unpkg.com/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">' in output
    assert '<script src="https://unpkg.com/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>' in output