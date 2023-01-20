from AppBuilder import AppBuilder


def demo():
    app = AppBuilder("MyApp") \
        .select() \
            .dataset("https://github.com/ABBARNABIL/zip-dataset/raw/main/input_data.zip") \
            .select("0", 1000) \
            .select("1", 1000) \
            .select("2", 1000) \
            .select("3", 1000) \
            .test_split(0.2) \
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
                .reshape_data("?", "?", 1) \
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
                    .values(128) \
                    .activation("relu") \
                .dense(4) \
                    .activation("stoftmax") \
                .compile() \
            .ANN() \
                .flatten_data() \
                .dense() \
                    .values(128) \
                    .activation("relu") \
                .dense(4) \
                    .activation("softmax") \
                .compile() \
            .end() \
        .compare() \
            .metrics() \
                .loss() \
            .when() \
                .accuracy(">  ", 0.5) \
            .end() \
        .build()

if __name__ == "__main__":
    demo()

"""
            .dataset("https://github.com/ABBARNABIL/zip-dataset/raw/main/input_data.zip") \

        .compare() \
            .metrics() \
                .accuracy() \
                .precision() \
            .when_accuracy(">", 0.5) \
                .and_precision(">", 0.5) \
                .and_loss("<", 0.5) \
        .deploy_best() \
"""
