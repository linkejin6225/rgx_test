# comp1的Makefile（依赖comp2的动态库）
LIBS = -lcomp2                  # 链接动态库（libb.so，省略前缀"lib"和后缀".so"）
TARGET ?= $(OUTPUT_DIR)/usr/bin/comp1              # 可执行文件目标

# 编译规则：依赖组件B的动态库
all: $(TARGET)

$(TARGET): comp1.c
	mkdir -p $(OUTPUT_DIR)/usr/bin/
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS) $(LIBS)

# 清理编译产物
clean:
	rm -f $(TARGET)
