try:
    1 / 0
except Exception as e:
    e.add_note('oh no!')
    raise


try:
    raise ExceptionGroup('', [
        ValueError(),
        KeyError('hello'),
        KeyError('world'),
        OSError(),
    ])
except* KeyError as e:
    print('caught1:', repr(e))
except* ValueError as e:
    print('caught2:', repr(e))
except* KeyError as e:
    1 / 0
