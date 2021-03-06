# coding=utf-8
class Config:
    def __init__(self):
        self.emb_dim = 200
        self.corpus_path = 'data/corpus.txt'
        self.train_corpus_path = 'data/train.txt'
        self.test_corpus_path = 'data/test.txt'
        self.model_path = 'data/chinese.model'
        self.raw_model_path = 'data/newsblogbbs.vec'
        self.dl_model_path = 'model/1228-150-3gram-with-test.model'
        self.max_sent_len = 28
        self.lstm_dim = 300
        self.n_filter = 300
        self.filter_size = 3
        self.dropout = 0.5
        self.l2_rate = 1e-3
        self.lr = 1e-3
        self.n_classes = 20
        self.h1_dim = 100
        self.batch_size = 32
        self.test_fold = 10
        self.epochs = 200
        self.result_path = 'data/results.txt'
        self.punc = u"！？。＂＃$＄％&＆'＇()（）*＊+＋，-－/／:：;；<＜=＝>＞@[［＼\］] \
            ＾^＿_｀`{｛|｜}｝~～《》｟｠｢｣､、〃「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟 \
            〰〾〿–—‘’‛“”„‟…‧﹏."
        self.class_dict = {'积分查询': 0,
                           '兑换积分': 1,
                           '优惠活动咨询': 2,
                           '流量包办理': 3,
                           '账单查询': 4,
                           '更改套餐': 17,
                           '积分兑换': 6,
                           '故障报修': 16,
                           '话费查询': 8,
                           '套餐变更': 9,
                           '套餐查询': 10,
                           '家庭礼包咨询': 11,
                           '查询积分': 12,
                           '修改密码': 13,
                           '密码修改': 19,
                           '流量查询': 15,
                           '套餐信息查询': 7,
                           '家庭礼包': 5,
                           '改密码': 18,
                           '挂失': 14,
                           }
        self.freq_words = ['我', '的', '我要', '了', '吗', '是', '想', '有','什么', '你', '你们', '吧', '呢', '啊']