# GITHUB

commit:
	git commit -am "commit from make file"

push:
	git push origin main

pull:
	git pull origin main

fetch:
	git fetch origin main

reset:
	rm -f .git/index
	git reset

req:
	pip freeze > requirements.txt

compush: commit push


# CONSOL RUN


run_no_debug:
	python main.py --no-debug

run:
	python main.py


# MODEL TUNING

tuning:
	python scripts/model_tuning.py


# predict.py fonksiyonunu kullanarak train seti değerleri tahmini ve AUC degeri
predict:
	python scripts/predict.py

# predict.py fonksiyonunu kullanarak test seti değerlerini tahmin etme
predict_test:
	python scripts/predict.py --test

# predict.py fonksiyonu ile tahmin edilen sonuçların kaggle'a gönderilmesi
submit:
	kaggle competitions submit -c home-credit-default-risk -f outputs/predictions/reference_submission.csv -m "Message"
