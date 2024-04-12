import requests
from pyfiglet import Figlet
import folium
import argparse

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="IP target")
    options=parser.parse_args()
    return options

def get_info_by_ip(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        try:
            area = folium.Map(location=[response.get('lat'), response.get('lon')])
            area.save(f'C:/Users/toart/Documents/Importantly/NET-Porgramming/inf_ips/{response.get("query")}_{response.get("city")}.html')
        except:
            print("Can't find a location")
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
        
        
def main():
    options=get_args()
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    if options.target!=None:
        get_info_by_ip(ip=str(options.target))
    else:
        ip = input('Please enter a target IP: ').split()
        for i in ip:
            if i!='':
                get_info_by_ip(ip=i)
    
    
if __name__ == '__main__':
    main()