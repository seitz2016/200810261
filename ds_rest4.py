key['dataseoul']
import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key=key['dataseoul']
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)