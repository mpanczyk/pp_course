SUB_TXT = $(wildcard *.md)
SUB_HTML = $(SUB_TXT:.md=.html)

all : $(SUB_HTML) index.html

%.html : %.md template.html transform.py
	./transform.py $< $@

index.html : index.html.template index.md make_index.py
	./make_index.py

clean:
	rm -f *~ *.backup
