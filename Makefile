SUB_TXT = $(wildcard topics/[0-9]*.md)
SUB_HTML = $(SUB_TXT:.md=.html)

all : $(SUB_HTML) index.html

%.html : %.md topic.html.template bin/transform.py
	bin/transform.py $< $@

index.html : index.html.template index.md bin/make_index.py
	bin/make_index.py

clean:
	rm -f *~ *.backup *.html topics/*.html
