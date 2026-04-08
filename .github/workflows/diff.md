这两份文件虽然都是用于 **自动部署 (GitHub Actions)**，但它们的设计思路、适用场景和复杂度是 **完全不同** 的。

简而言之：

* **`deploy.yml` (基础版)**：适合 **单仓库** 模式。假设您的 Wiki 所有内容（文档、图片）都直接放在这个仓库里。
* **`publish.yml` (进阶聚合版)**：适合 **多仓库** 模式。Wiki 只是一个“壳”，它会自动去拉取您其他产品仓库（如 5寸屏代码库、7寸屏代码库）里的 `README.md`，把它们“组装”成 Wiki。

以下是详细对比：

### 1. 核心逻辑区别 (Core Logic)

| 特性 | **deploy.yml (单体模式)** | **publish.yml (聚合模式)** |
| --- | --- | --- |
| **内容来源** | **当前仓库**。MkDocs 直接构建当前目录下的 `docs/`。 | **6个不同的仓库**。它会从 `repo-7inch`, `repo-5inch` 等仓库拉取代码。 |
| **预处理** | **无**。直接 Build。 | **极强**。包含一段复杂的 Shell 脚本，负责复制文件、重命名、移动图片、修改图片路径。 |
| **触发机制** | 仅 `push` 到 main 分支。 | `push` + `repository_dispatch` (允许别的仓库更新时，远程通知这边更新)。 |
| **依赖插件** | 基础的 `mkdocs-material`。 | 包含 `mkdocs-static-i18n` (多语言) 和 `minify` (压缩)，且有防冲突安装脚本。 |

### 2. 关键代码段解析

#### `publish.yml` 里的“组装工厂” (最复杂的部分)

`publish.yml` 中有一大段 `Assemble Content` 脚本，这是它的核心黑科技：

```bash
# 这段脚本的作用是：
# 1. 把别人仓库里的 README.md 拿过来，改名为 esp32-p4-7inch.md
# 2. 把别人仓库里的 assets 图片拿过来，放到 wiki 的 assets 目录下
# 3. 这里的 sed 命令非常关键：它会自动把文档里写死的 "assets/" 路径替换成 Wiki 需要的 "../../assets/..." 路径
sed -i "s|assets/|../../assets/images/products/$img_subdir/|g" ...

```

**意义**：这意味着您的产品工程师只需要维护产品仓库的 README，Wiki 会自动同步更新，不需要人工复制粘贴。

### 3. FTP 部署配置的区别 (风险点)

这里有一个非常重要的细节差异，直接关系到您的文件会不会被误删。

* **`deploy.yml` (安全)**：
```yaml
exclude: |
  downloads/**
  images/**

```


它配置了 `exclude`，**保护了服务器上的大文件**（如您手动上传的 PDF）。
* **`publish.yml` (有风险)**：
它 **没有** 配置 `exclude` 参数。
如果直接使用这个文件，SiteGround 上原本存在的 `downloads` 文件夹可能会被 **直接删除**！

### 4. 目录结构的区别

* **`deploy.yml`**: 认为 `mkdocs.yml` 就在根目录下。
* `local-dir: ./site/`


* **`publish.yml`**: 认为 Wiki 源码在一个子目录里（因为它先 checkout 到了 `wiki` 文件夹）。
* `working-directory: ./wiki`
* `local-dir: ./wiki/site/`



### 🏆 总结与建议

#### 情况 A：如果您现在刚开始建站，且手动管理内容

**请使用 `deploy.yml**`。
它是最标准的配置，简单、稳定，且包含了防止误删大文件的保护机制。您只需要手动写 Markdown 即可。

#### 情况 B：如果您想实现“代码库更新，Wiki 自动变”

**请使用 `publish.yml`，但必须修改！**
这个文件非常高级，适合后期维护。如果您决定用它，必须做以下修改才能运行：

1. **添加保护**：在最后的 FTP 步骤中，把 `deploy.yml` 里的 `exclude` 配置复制过去。
2. **确认路径**：确保您的 SiteGround 目录路径是 `/displaywiki.tech/public_html/` 还是直接 `/public_html/`。
3. **确认仓库名**：脚本里写死了 `VIEWESMART/7-1024X600-ESP32-P4-C6-TOUCH-DISPLAY` 等仓库名，您必须确保这些仓库真实存在且公开，否则会报错。

**我的建议：**
先用 **`deploy.yml`** 跑通流程，确保网站能上线。等未来产品线多了，觉得手动复制文档太累了，再升级到 `publish.yml` 的自动化聚合模式。