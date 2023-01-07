from AppBuilder import AppBuilder

def demo():
    app = AppBuilder("MyApp") \
        .select() \
            .select("0", 100) \
            .select("1", 200) \
            .test_size(0.2) \
            .end() \
        .transform() \
            .flatten()\
            .normalize() \
            .end() \
        .create_model() \
            .ANN() \
               .dense(512) \
               .dense(10, "softmax") \
               .compile() \
            .end() \
        .build()
    print(app)

if __name__ == "__main__":
    demo()