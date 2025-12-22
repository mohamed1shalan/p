import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing import sequence

max_features = 10000
max_len = 200

(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=max_features)

print(len(input_train), 'train')
print(len(input_test), 'test')

input_train = sequence.pad_sequences(input_train, maxlen=max_len)
input_test = sequence.pad_sequences(input_test, maxlen=max_len)

model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(64, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])

print('Train...')
model.fit(input_train, y_train, batch_size=32, epochs=5,
          validation_data=(input_test, y_test))

score, acc = model.evaluate(input_test, y_test, batch_size=32)
print('Test score:', score)
print('Test accuracy:', acc)
model.save('my_sentiment_model.keras')

# Loading data...
# 17464789/17464789 ━━━━━━━━━━━━━━━━━━━━ 0s 0us/step
# 25000 train 
# 25000 test 
# Pad sequences (samples x time)...
# Train...
# Epoch 1/5
# 782/782 ━━━━━━━━━━━━━━━━━━━━ 584s 736ms/step - accuracy: 0.7134 - loss: 0.5357 - val_accuracy: 0.8134 - val_loss: 0.4267
# Epoch 2/5
# 782/782 ━━━━━━━━━━━━━━━━━━━━ 622s 796ms/step - accuracy: 0.8519 - loss: 0.3514 - val_accuracy: 0.8207 - val_loss: 0.4123
# Epoch 3/5
# 782/782 ━━━━━━━━━━━━━━━━━━━━ 568s 727ms/step - accuracy: 0.8766 - loss: 0.3106 - val_accuracy: 0.8447 - val_loss: 0.3611
# Epoch 4/5
# 782/782 ━━━━━━━━━━━━━━━━━━━━ 566s 724ms/step - accuracy: 0.9069 - loss: 0.2362 - val_accuracy: 0.8601 - val_loss: 0.3618
# Epoch 5/5
# 782/782 ━━━━━━━━━━━━━━━━━━━━ 561s 718ms/step - accuracy: 0.9242 - loss: 0.1968 - val_accuracy: 0.8538 - val_loss: 0.3702
# 782/782 ━━━━━━━━━━━━━━━━━━━━ 89s 114ms/step - accuracy: 0.8499 - loss: 0.3784
# Test score: 0.37024614214897156
# Test accuracy: 0.8538399934768677