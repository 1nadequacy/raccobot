import numpy as np
import brain
import dataset
import argparse

TEMPERATURES = [0.2, 0.5, 1.0, 1.2]

def sample(p, temp=1.0):
    p = np.log(p) / temp
    p = np.exp(p) / np.sum(np.exp(p))
    return np.argmax(np.random.multinomial(1, p, 1))


def validate(model, data, length=80):
    phrase = data.get_random_phrase()
    print 'init phrase: %s' % phrase
    for temp in TEMPERATURES:
        result = str(phrase)
        s = str(phrase)
        for _ in range(length):
            x = data.phrase_to_x(s)
            p = model.predict(x, verbose=0)[0]
            char = data.get_char(sample(p, temp))
            result += char
            s = s[1:] + char
        print 'temperature %.1f: %s' % (temp, result)


def main(model_name, data_set_file, num_epochs):
    print 'loading data set %s' % data_set_file
    data = dataset.DataSet(data_set_file)
    X, y = data.get_data()
    print 'build model'
    model = brain.build_nn(X[0].shape, y[0].shape[0])
    model.summary()

    for epoch in range(num_epochs):
        print 'epoch %s' % epoch
        print 'training'
        model.fit(X, y, batch_size=128, nb_epoch=1)

        print 'validating'
        validate(model, data)

        brain.save_model(model,'%s_%s' % (model_name, epoch))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('model_name')
    parser.add_argument('data_set')
    parser.add_argument('--num_epochs', default=50)
    parser.add_argument('--explr_eps', default=0.1)
    args = parser.parse_args()

    main(args.model_name, args.data_set, int(args.num_epochs))
