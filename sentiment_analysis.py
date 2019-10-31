def extract_features(word_list):
    return dict([(word, True) for word in word_list])


def get_predictions(posts, classifier):
    """
    Generate sentiment analysis of a given text
    :param posts: list; list of posts scraped from nairaland
    :param classifier: model
    :return: predicted sentiment, positive or negative
    """
    predictions = []
    for text in posts:
        features = dict([(word, True) for word in text.split()])
        probability_dist = classifier.prob_classify(features)
        prediction_sentiment = probability_dist.max()
        if prediction_sentiment == 'Positive':
            predictions.append(1)
        else:
            predictions.append(0)
    avg_prediction = round(sum(predictions) / len(predictions))
    if avg_prediction == 1:
        return "Positive"
    else:
        return 'Negative'

