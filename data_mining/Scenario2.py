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
                .reshape_data("?", "?", 1) \
                .conv(32) \
                    .kernel_size(3,3) \
                    .activation("relu | sigmoid") \
                .conv(48) \
                    .kernel_size(3,3) \
                    .activation("relu | sigmoid") \
                .max_pooling(2,2) \
                .flatten() \
                .dense()\
                    .values(128) \
                    .activation("relu | sigmoid") \
                .dense(5) \
                    .activation("stoftmax") \
                .compile() \
            .end() \
        .compare() \
            .metrics() \
                .accuracy() \
            .when() \
                .accuracy(">=", 0.5) \
            .end() \
        .deploy_best("My Prediction App Scenario2") \
        .build()
