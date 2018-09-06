import requests


def sendRequest(ip, port, route, data=None, protocol="http"):
    url = "{protocol}://{ip}:{port}{route}".format(protocol=protocol, ip=ip, port=port, route=route)

    if data is not None:
        try:
            resp = requests.post(url, data=data)

        except requests.HTTPError as e:
            raise PipelineServiceError("{reason}".format(reason=e))

    else:
        try:
            resp = requests.get(url)

        except requests.HTTPError as e:
            raise PipelineServiceError("{reason}".format(reason=e))

    return resp
