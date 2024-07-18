import requests

def getApiResponse():
    header = {
        "Host": "ollehtvplay.ktipmedia.co.kr",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Accept": "application/json",
        "User-Agent": "GTP(compatible;ServiceType/GTVM;OSType/iOS;DeviceModel/iPhone 12 Pro Max;OSVersion/17.4.1;AppName/GenieTvMobile;AppVersion/1.1.6)",
        "Content-Length": "247",
        "Accept-Encoding": "gzip, deflate, br",
    }
    cookie = {"SCOUTER": "z45tf24hdqk5nj"}
    response = requests.post(
        "https://ollehtvplay.ktipmedia.co.kr/otp/gtm/epg/list",
        data='{"DATA":"SJyTDWaaKiCo6Xjz019EvbwnX8GjrhqMbdMHwPNOnJl4MXDmwcmYSjYj8XM0mQYgMWnEovdVOQaKhZie96kMwWzo841pHIgRYRIhWYeWpi/pLJdNo15j4jlNpk1Y0RPbLSsT9WQCx8EOIsvmkbHh4Kip6dSS1OuC7fQLqqj1GahhRutjaKOMWjCT2VNcN/o2lS0AYfxP6RR9kMcxWkXau1m4v71BNtoOsONTyD87oiY="}',
        cookies=cookie,
        headers=header,
        verify=False,
    )
    return response.json()

if __name__=="__main__":
    getApiResponse()
