from AppBuilder import AppBuilder

AppBuilder("MyApp") \
        .select() \
            .acquire_data("https://github.com/ABBARNABIL/zip-dataset/raw/main/input_data.zip") \
            .class_("0", 1000) \
            .class_("1", 1000) \
            .class_("2", 1000) \
            .class_("3", 1000) \
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
            .all_metrics() \
            .end() \
        .deploy_best("My Prediction App") \
        .build()