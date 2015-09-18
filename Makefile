SUB_TXT = $(wildcard *.txt)
SUB_HTML = $(SUB_TXT:.txt=.html)

all : $(SUB_HTML) index.html

%.html : %.txt template.html transform.py
	./transform.py $< $@

index.html : index.html.template index.txt.template make_index.py
	./make_index.py

clean:
	rm -f *~ *.backup
