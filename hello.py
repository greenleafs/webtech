
def application(env, start_response):
    """Hello app."""
    query_string = env.get('QUERY_STRING', '')
    start_response('200 OK', [('Content-type', 'text/plain')])
    if query_string:
        return ['{}\n'.format(item) for item in query_string.split('&')]
    else:
        return []
