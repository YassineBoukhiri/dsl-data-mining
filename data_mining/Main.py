from AppBuilder import AppBuilder

def demo():
    app = AppBuilder("MyApp") \
        .select() \
            .select("0", 1000) \
            .select("1", 1000) \
            .select("2", 1000) \
            .select("3", 1000) \
            .test_size(0.2) \
            .end() \
        .preprocess() \
            .fit() \
            .end() \
        .transform() \
            .normalize() \
            .reshape("?", "?", 1) \
            .end() \
        .create_model() \
            .CNN() \
                .conv(32) \
                    .kernel_size(3,3) \
                    .activation("relu") \
                .max_pooling(2,2) \
                .conv(48) \
                    .kernel_size(3,3) \
                    .activation("relu") \
                .max_pooling(2,2) \
                .flatten() \
                .dense()\
                    .values(128, 256) \
                    .activation("relu") \
                .dense(4) \
                    .activation("softmax") \
                .compile() \
            .end() \
        .build()

if __name__ == "__main__":
    demo()

'''.CNN() \
    .conv(32) \
        .kernel_size(3,3) \
        .activation("relu") \
    .max_pooling(2,2) \
    .conv(48) \
        .kernel_size(3,3) \
        .activation("relu") \
    .max_pooling(2,2) \
    .dropout(0.5) \
    .flatten() \
    .dense(128) \
        .activation("relu") \
    .dense(4) \
        .activation("softmax") \
    .compile() \
.end() \" '''


'''.
() \
    .dense() \
        .values(32, 64, 128) \
        .activation("relu") \
    .dense(4) \
        .activation("softmax") \
    .compile() \
.end() \''''