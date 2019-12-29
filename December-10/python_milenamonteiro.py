def cookieCount(n, p, c):
    cookies_eaten = jars_left = n // p
    while jars_left >= c:
        result = divmod(jars_left, c)
        jars_left -= c
        cookies_eaten += result[0]
        jars_left += result[1]
    return cookies_eaten
