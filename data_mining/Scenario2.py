from AppBuilder import AppBuilder

AppBuilder("Scenario 2") \
        .select() \
            .all_classes() \
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
                .conv(32) \
                    .kernel_size(3,3) \
                    .activation("relu | sigmoid") \
                .max_pooling(2,2) \
                .conv(48) \
                    .activation("relu | sigmoid") \
                .max_pooling(2,2) \
                .flatten() \
                .dense()\
                    .values(128) \
                    .activation("relu | sigmoid") \
                .dense(10) \
                    .activation("softmax") \
                .compile() \
            .end() \
        .compare() \
            .all_metrics() \
            .when() \
                .accuracy(">=", 0.5) \
                .loss("<=", 0.5) \
            .end() \
        .deploy_best("My Prediction App Scenario2") \
        .build()
