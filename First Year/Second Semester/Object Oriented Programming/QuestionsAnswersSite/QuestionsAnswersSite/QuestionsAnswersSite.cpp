#include "QuestionsAnswersSite.h"

QuestionsAnswersSite::QuestionsAnswersSite(service& s, QWidget *parent)
    : QMainWindow(parent), s(s)
{
    ui.setupUi(this);
    connectSignalsAndSlots();
}

QuestionsAnswersSite::~QuestionsAnswersSite()
{}

void QuestionsAnswersSite::findBestMatch()
{
    string input = this->ui.lineEdit->text().toStdString();
    string text;
    int max_score = 0;
    int idq;
    for (question q : s.getQuestions()) {
        int score = 0;
        int l = std::min(q.getText().length(), input.length());
        for (int i = 0; i < l; i++){
            if (input[i] == q.getText()[i]) score++;
        }
        
        if (score > max_score) {
            max_score = score;
            text = q.getText();
            idq = q.getId();
        }
    }
    this->ui.listWidget->clear();
    this->ui.listWidget_2->clear();
    this->ui.listWidget->addItem(QString::fromStdString(text));
    vector<answer> answers = s.getAnswers();
    std::sort(answers.begin(), answers.end(),
        [](answer a, answer b) {return a.getVotes() > b.getVotes(); });
    int c = 0;
    for (answer a : answers) {
        if (c < 3) {
            if (a.getIdQuestion() == idq) {
                this->ui.listWidget_2->addItem(QString::fromStdString(a.getText() + '|' + std::to_string(a.getVotes())));
                c++;
            }
        }
        else break;
    }
}

void QuestionsAnswersSite::connectSignalsAndSlots()
{
    QObject::connect(this->ui.lineEdit, &QLineEdit::textChanged, this, &QuestionsAnswersSite::findBestMatch);

}

