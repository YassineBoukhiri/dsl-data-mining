from AppBuilder import AppBuilder

AppBuilder("Scenario1") \
        .select() \
            .acquire_data("https://github.com/ABBARNABIL/zip-dataset/raw/main/input_data.zip") \
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
            .ANN() \
                .flatten_data() \
                .dense() \
                    .values(128, 256) \
                    .activation("relu | softmax | sigmoid") \
                .dense() \
                    .values(128) \
                    .activation("relu | sigmoid") \
                .dense(4) \
                    .activation("softmax") \
                .compile() \
            .end() \
        .compare() \
            .all_metrics() \
            .end() \
        .deploy_best("My Prediction App for Scenario 1") \
        .build()
