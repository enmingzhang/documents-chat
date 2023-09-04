import requests
import json

url = 'http://nlp.ai.dev.valuesimplex.tech/api/ml/get_seg_max_m3e_embedding'
headers = {"Content-Type": "application/json"}
data_dict = {
    "content": [
        "像整个塔筒这边其实是一个成本加成的盈利模式，像龙头公司的出货还保持一个非常快速的增长，因为整个它们大概是有一个外公里的运输半径，所以各个公司在各个省份的布局就会显得尤其重要，所以我们判断整个传统的盈利能力相对来讲后续比较稳定。如果是农村也比较强，布局比较好的这些公司，也要是得到一个快速的放量。 \n同时如果有一些海外港口，比如说我们这里码头可以直接出口海外的，被直接带来一定的盈利能力的控制系统，海外的单边净利基本上比国内是高了是200~300左右的水平，而且有码头出口不仅可以做出口，还可以做一些海上风的专注件。废除率来讲，一些采访公司后续的概念在于海外和海外的这么一个量。  另外在海底基桩上来讲，这里未来的需求量会越来越多，因为之前主要做的其实是陆风以及是在近海的风往后面，会有外远风，我看远上来就是远海来做，远海来做。基本上包括单桩导光导桩架也是漂浮式等一系列的对应使用量。  由于你的海水的深度越深，你对应的海底的一个激光管道量就会越来越大，所以你对应的整个海缆也会非常越来越多，所以我们判断整个海上基础需求达到了2025，有个560万吨左右的水平，而在2022年基本上只能做到250万水平，经常会有一个是翻一倍的量，所以从这个角度上来讲，厂商后面的一些的管装就会显得尤其重要。  最后我们把整个标的做了一个梳理，包括是几条有线对应下来，海上海外国产地带，因为明年的量预计是有70g瓦以上的水平，而陆丰占比相对高一些，我们判断海丰这条线占比相对来讲会盈利好一些，对应海上风电这条线，包括东方电缆、豪放电器以及是明阳智能，相对来讲是大金重工是相对来讲确定性比较强的。 在整个海外这条线主要包括是金雷、日月、天顺我们判断他们都是有很大的强的出口能力，在整个国产替代这条线上，包括新强联、恒瑞，他们也是有一个比较强的能力，所以大概是这个情况，我这边的汇报主要是这些。主持人。好的，十分感谢张磊老师的精彩演讲。接下来我们进入互动问答环节，请大家将您的问题通过直播间下方交流区发送给我们，请注意合规性原因，有关个股咨询的问题将被删除。1~3分钟之后我们将开始进入问答环节。天使十分感谢各位观众的踊跃回答，踊跃提问，我这边已经收到了第一个问题是来自投资田毅的问题，风电产业链中上中下游分别的竞争格局和竞争态势如何，各企业如何构建自己的行业壁垒？有请张磊老师。 整个风电产业链相对来讲是比较短的，包括整个下游的整机以及上游的零部件这么短的情况，不同环节的整个建立壁垒的方式也是不太一样。我们这边认为在整机端更重要的是研发以及是你和向下游的客户关系相对来讲确定性是最重要的。另外你的出口能力也会变得是尤其的这么一个重要。我们判断在整机端上来讲，第一长期的客户积累是最重要的一个环节。另外一点是你整个的资金实力也会成为一个比较重要的点。  而对于整个偏零部件环节不同的也是不一样的，像基础加工类的，其实就考察基础加工的能力，非技术加工类，我们判断你整个的这么一个，比如说你是有机物跟有机物的一个处理能力到底怎么样，我们看到这些的变化其实都是非常确定的。 所以从这个角度上来讲，零部件这边像海买它要看它的一个码头的资源，像住建这边也考虑它大型化的资源以及成本控制的能力，所以从这个角度上来讲，整个风风电的不同环节是不一样的，在供应节点，因为风电的资产相对偏重资产，一方面考验资金实力，第二产能产量的布局，第三是你的客户结构，所以我们认为这几点相对来讲是整个风电构建壁垒更强的几个点，如果你所谓的有排他性的一些资源的限制，比如说在广东这边一些企业可能就会有一些差异化的竞争优势，所以这个也是比较大的一个点，我回答主要是这些。 好的，十分感谢张磊老师的回答。"
    ]
}

res = requests.post(url=url, headers=headers, json=data_dict)
print(res.text)
res = json.loads(res.text)['prediction']['data']

print(len(res[0]['embedding'][0]))
print(res[0]['sentences'][0])
print("\n")
print(len(res[0]['embedding'][1]))
print(res[0]['sentences'][1])
print("\n")
print(len(res[0]['embedding'][2]))
print(res[0]['sentences'][2])
print("\n")
print(len(res[0]['embedding'][3]))
print(res[0]['sentences'][3])
print("\n")
print(len(res[0]['embedding'][4]))
print(res[0]['sentences'][4])
