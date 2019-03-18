import requests

resp = requests.get('http://183.134.64.20/videos/v1/20180922/15/bb/c7f9b6a2ea42aaa32304174bb17d114f.mp4?key=0af38f0ba70744a499a50ec3839f12aac&dis_k=20cfae16f4700293275968c72b140b9b8&dis_t=1537954050&dis_dz=CT-ZheJiang_HangZhou&dis_st=40&src=iqiyi.com&uuid=a7957a5-5bab5102-b3&m=v&qd_k=0db8fe83dd19104e45a444485ee10fdf&sgti=&qd_ip=7237e00c&qd_p=7237e00c&dfp=&qd_src=02020031010000000000&ssl=&ip=114.55.224.12&qd_vip=0&dis_src=vrs&qd_uid=0&qdv=1&qd_tm=1537954050671')

with open('a.mp4','wb') as f:
    f.write(resp.content)