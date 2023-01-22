from AppBuilder import AppBuilder

AppBuilder("Scenario3") \
        .select() \
            .acquire_data("https://github.com/ABBARNABIL/zip-dataset/raw/main/input_data.zip") \
            .all_classes() \
            .test_split(0.2) \
            .end() \
        .preprocess() \
            .fit() \
            .end() \
        .transform() \
            .normalize() \
            .reshape("28", "28", 1) \
            .end() \
        .create_model() \
            .CNN() \
                .reshape_data("?", "?", 1) \
                .conv(32) \
                    .kernel_size(3,3) \
                    .activation("relu | sigmoid | softmax") \
                .max_pooling(2,2) \
                .conv(48) \
                    .kernel_size(3,3) \
                    .activation("relu | sigmoid | softmax") \
                .max_pooling(2,2) \
                .flatten() \
                .dense()\
                    .values(128) \
                    .activation("relu | sigmoid | softmax") \
                .dense(10) \
                    .activation("stoftmax") \
                .compile() \
            .ANN() \
                .flatten_data() \
                .dense() \
                    .values(128) \
                    .activation("relu | sigmoid | softmax") \
                .dense(10) \
                    .activation("softmax") \
                .compile() \
            .end() \
        .compare() \
            .all_metrics() \
            .end() \
        .deploy_best("My Prediction App Scenario3") \
        .build()