from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
import pandas as pd
from tqdm import tqdm

class Embedder:
    """
    A class to handle embedding of documents and uploading them to a Qdrant collection.

    Attributes:
        qdrant (QdrantClient): The Qdrant client instance.
        encoder (SentenceTransformer): The sentence transformer model for encoding text.
        data_source (str): Path to the CSV file containing the data.
        question_column (str): The column name in the data source for questions.
        answer_column (str): The column name in the data source for answers.
        db_name (str): The name of the Qdrant collection.
        documents (list): A list of dictionaries containing questions and answers.

    Methods:
        load_data():
            Loads data from the CSV file and prepares documents for embedding.
        create_collection():
            Creates a new collection in Qdrant with the specified configuration.
        upload_documents():
            Uploads the encoded documents to the Qdrant collection.
    """
    
    def __init__(self, data_source, question_column_in_data_source, answer_column_in_data_source, db_name, qdrant_link="http://localhost:6333", encoder_name="all-MiniLM-L6-v2", auto_load=False):
        self.qdrant = QdrantClient(qdrant_link)
        self.encoder = SentenceTransformer(encoder_name)
        self.data_source = data_source
        self.question_column = question_column_in_data_source
        self.answer_column = answer_column_in_data_source
        self.db_name = db_name

        if auto_load:
            self.load_data()
            self.create_collection()
            self.upload_documents()

    def load_data(self):
        self.df = pd.read_csv(self.data_source, dtype=str, low_memory=False)
        print("Data loading ...")
        self.documents = [{"question": q, "answer": self.df[self.answer_column].tolist()[idx]} for idx, q in tqdm(enumerate(self.df[self.question_column].tolist()), total=len(self.df[self.question_column].tolist()))]

    def create_collection(self):
        self.qdrant.delete_collection(collection_name=self.db_name)
        self.qdrant.create_collection(
            collection_name=self.db_name,
            vectors_config=models.VectorParams(
                size=self.encoder.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
            ),
        )
        print("Creating collection in Qdrant ...")

    def upload_documents(self):
        for idx, doc in tqdm(enumerate(self.documents), total=len(self.documents)):
            self.qdrant.upload_points(
                collection_name=self.db_name,
                points=[
                    models.PointStruct(
                        id=idx, vector=self.encoder.encode(doc["question"]).tolist(), payload=doc
                    )
                ],
            )
        print("Embedding database created successfully!")

# Usage
# embedder = Embedder(
#     data_source='data/sierra_db.csv',
#     question_column='UserQuestion',
#     answer_column='ModelAnswer',
#     db_name='sierra_db',
#     auto_load=True
# )