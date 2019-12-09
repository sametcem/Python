import  urllib.request

url1="https://iatkv.tmgrup.com.tr/590311/616/321/0/0/561/292?u=https://itkv.tmgrup.com.tr/2019/01/14/muhayer-oktay-kimdir-besiktasin-yeni-transferi-muhayer-oktay-kac-yasinda-1547460127828.jpg"
url2="https://img.fanatik.com.tr/img/78/740x418/5c25b15366a97cc6a4209dcc"


urllist=[url1,url2]
count=1

for url in urllist:
    urllib.request.urlretrieve(url,"Resim" + str(count)+".jpg")
    count+=1

urlv ="https://www.youtube.com/watch?v=EU8zBEzDNEY&list=PLIHume2cwmHehcxQE1XZieL21syR3m3tR&index=25"
urllib.request.urlretrieve(urlv,"video")