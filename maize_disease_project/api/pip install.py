import tensorflow as tf
try:
    model = tf.keras.models.load_model(r"C:\Users\Admin\Desktop\maize_disease_project\saved_models\my_corn_disease_model.keras")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error: {e}")