from AppBuilder import AppBuilder


def demo():
    app = AppBuilder("MyApp") \
        .select() \
        .dataset("../input_data") \
        .select("0", 100) \
        .select("1", 100) \
        .test_size(0.2) \
        .end() \
        .preprocess() \
        .fit() \
        .end() \
        .transform() \
        .flatten()\
        .normalize() \
        .end() \
        .create_model() \
        .ANN() \
        .dense(512) \
        .dense(2, "softmax") \
        .compile() \
        .end() \
        .build()


if __name__ == "__main__":
    demo()
