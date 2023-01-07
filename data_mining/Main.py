from AppBuilder import AppBuilder

def demo():
    app = AppBuilder("MyApp") \
        .select() \
            .select("0", 100) \
            .select("1", 200) \
            .test_size(0.5) \
            .end() \
        .transform() \
            .resize(100, 100) \
        .build()

    print(app)

if __name__ == "__main__":
    demo()