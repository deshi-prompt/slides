# Makefile for *.dot --> *.png

BUILD_DIR= fig
SRC_DIR= src
TEMPLATE_DIR=`pwd`/template

DOT_SRCS= $(wildcard src/*.dot)
PNG_TGTS= $(patsubst src/%.dot,${BUILD_DIR}/%.png,$(DOT_SRCS))

.SUFFIXES:
.SUFFIXES: .dot .png

$(PNG_TGTS):$(DOT_SRCS)
	dot -Tpng $< -o$@

#$(BUILDDIR)/%.png: %.dot
#	@[ -d $(BUILDDIR) ]
#	$(COMPILER) $(CFLAGS) $(INCLUDE) -o $@ -c $<

dot2png: ${PNG_TGTS}
all: dot2png

.PHONY: list
list:
	@echo sources dot : ${DOT_SRCS}
	@echo ""
	@echo targets png : ${PNG_TGTS}

.PHONY: clean
clean:
	@rm -f ${PNG_TGTS}

