# 部署说明

## 方法一：Cloudflare Pages 后台手动上传（最简单）

1. 登录 https://dash.cloudflare.com/ 
2. 进入 **Pages** → 选择 **1hcrypto** 项目
3. 点击 **Deployments** → **Upload assets**
4. 选择 `G:\workbuddy\2026-05-29-15-38-18\1hcrypto\dist\` 目录下的所有文件
5. 上传完成后点击 **Promote to Production**

## 方法二：重新生成 API Token 后自动部署

如果要用命令行自动部署，需要重新生成一个有正确权限的 API Token：

1. 登录 https://dash.cloudflare.com/profile/api-tokens
2. 点击 **Create Token**
3. 权限选择：
   - `Account - Cloudflare: Read`（读取账户信息）
   - `Account - Cloudflare Pages: Edit`（部署 Pages）
4. 生成后，在 WorkBuddy 中运行：
   ```bash
   cd "G:/workbuddy/2026-05-29-15-38-18/1hcrypto"
   export CLOUDFLARE_API_TOKEN="你的新Token"
   npx wrangler pages deploy dist/ --project-name=1hcrypto --branch=main
   ```

## 当前构建状态

✅ 构建成功：117 个页面，0 错误
✅ 模拟盘页面已恢复（资产总额图、净值曲线、进阶指标）  
✅ 文章详情页路由已修复  
📁 构建输出目录：`G:\workbuddy\2026-05-29-15-38-18\1hcrypto\dist\`
