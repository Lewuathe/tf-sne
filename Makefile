all:
	docker build -t lewuathe/tf-sne .

.PHONY: test clean

run:
	docker run -it -p 6006:6006 -v ${DATA_DIR}:/srv/tf-sne/data lewuathe/tf-sne ${OPTIONS}
