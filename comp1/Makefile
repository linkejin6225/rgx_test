# comp1的Makefile（依赖comp2的动态库）
LIBS = -lcomp2
TARGET = $(OUTPUT_DIR)/usr/bin/comp1
TARGET_SH = $(OUTER_DIR)/hello

# 编译规则：依赖组件B的动态库
all: $(TARGET)

$(TARGET): comp1.c
	mkdir -p $(OUTPUT_DIR)/usr/bin/
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS) $(LIBS)

$(TARGET_SH): hello.sh
	shc -f $< -r -o hello
	$(CC) hello.c -o $@
	rm -rf hello.c hello

install: $(TARGET)
	cp -r ./scripts $(OUTPUT_DIR)
	mkdir -p $(OUTPUT_DIR)/opt/test/
	cp ./myapp.py $(OUTPUT_DIR)/opt/test/
