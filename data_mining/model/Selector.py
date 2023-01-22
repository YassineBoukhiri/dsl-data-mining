from model.Class import Class
from model.Notebookable import Notebookable
from model.Cell import CELL_TYPE
import os
import urllib
from io import BytesIO
from zipfile import ZipFile


class Selector(Notebookable):

    def __init__(self):
        super().__init__()
        self.dataset = "input_data"
        self.classes = []
        self.test_size = 0.2

    def __repr__(self):
        result = ""
        for i, class_ in enumerate(self.classes):
            result += class_.__repr__() + "\n" if i != len(self.classes) - \
                1 else class_.__repr__()
        return result

    def add_class(self, class_: Class):
        self.classes.append(class_)

    def set_test_size(self, test_size: float):
        if test_size < 0 or test_size > 1:
            raise Exception("Test size must be between 0 and 1.")
        if test_size > 0.4:
            print("Warning : test size is too big.")
        self.test_size = test_size

    def set_dataset(self, dataset: str):
        if "http" in dataset:
            print("INFO: Downloading dataset...")
            resp = urllib.request.urlopen(dataset)
            zipfile = ZipFile(BytesIO(resp.read()))
            dataset_dir = zipfile.namelist()[0].split("/")[0]
            if os.path.exists(dataset_dir):
                print("INFO: Dataset already exists.")
                self.dataset = dataset_dir
                return
            zipfile.extractall()
            print("INFO: Dataset downloaded.")
            self.dataset = dataset_dir
        self.dataset = dataset

    def get_notebook(self) -> str:
        self.add_cell(CELL_TYPE.MARKDOWN,
                      """## Selection of data""")
        self.add_cell(
            CELL_TYPE.CODE, """import os\nimport numpy as np\nfrom PIL import Image""")
        code = "X = []\nY = []\n"\
            + "classes = [" + ", ".join([f"'{class_.name}'" for class_ in self.classes]) + "]\n"\
            + "classes_count = {" + ", ".join([f"'{class_.name}': {class_.count}" for class_ in self.classes]) + "}\n"\
            + "for class_ in classes:\n"\
            + "\tcount = 0\n"\
            + "\tfor file in os.listdir(f'" + self.dataset + "/" + "' + class_):\n"\
            + "\t\tif count == classes_count[class_]:\n"\
            + "\t\t\tbreak\n"\
            + "\t\tX.append(np.array(Image.open(f'" + self.dataset + "/" + "' + class_ + '/' + file)))\n"\
            + "\t\tY.append(class_)\n"\
            + "\t\tcount += 1\n"\
            + "X=np.array(X)\n"\
            + "Y=np.array(Y)\n"\
            + "print(\"X shape :\",X.shape)\n"\
            + "print(\"Y shape :\",Y.shape)"
        self.add_cell(CELL_TYPE.CODE, code)
        self.add_cell(CELL_TYPE.CODE, """from sklearn.model_selection import train_test_split\nX_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=""" + str(self.test_size) + """)""")
        return super().get_notebook()
