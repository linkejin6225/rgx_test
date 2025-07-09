# comp2的Makefile（生成动态库）
CFLAGS = -Wall -Wextra -fPIC  # -fPIC：位置无关代码（动态库必需）
LDFLAGS = -shared             # -shared：生成动态库
TARGET = $(OUTPUT_DIR)/usr/lib/libcomp2.so              # 动态库目标文件（命名规则：libxxx.so）

# 编译规则：生成动态库
all: $(TARGET)

$(TARGET):comp2.c comp2.h
	mkdir -p $(OUTPUT_DIR)/usr/lib/
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

install: $(TARGET)
	cp -f $(TARGET) $(IMAGES_LIB)
	cp -f ./comp2.h $(IMAGES_INCLUDE)
	cp -r ./scripts $(OUTPUT_DIR)

# 清理编译产物
clean:
	rm -f $(TARGET)
