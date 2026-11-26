# 動画からモーションキャプチャ「RGB MoCap」— Blender／Unrealへ連携できるWindowsアプリ

- 日付: 2026-11-23
- 作者: Bigger-Parker @biggerparker.cos（Threads）
- カテゴリ: AIツール／モーションキャプチャ
- 元ネタ: https://www.threads.com/@biggerparker.cos/post/DgHVKBLD7Id
- リポジトリ: https://github.com/toyxyz/toyxyz_RGBMocap

## 要約

Threads のカルーセル投稿（英語）。「動画からモーションキャプチャができるなんて」という紹介で、GitHub リポジトリ toyxyz/toyxyz_RGBMocap を共有している。作者は開発者ではなく、コメント欄で「自分は開発者ではなく、リポジトリを紹介しているだけ」と補足している。

リポジトリの README で裏取りした内容は次のとおり。RGB MoCap は、動画を編集可能な人物アニメーションに変換する Windows ネイティブアプリで、AI 処理はローカルで動く。

- 姿勢推定モデルは ExMR／FlowHMR／GVHMR が基本。任意で PromptHMR、MAMMA（マルチカメラ用）、GEM-X、PEAR（Webカメラ等のリアルタイムプレビュー、実験的）も追加できる
- 足・手の接地ずれを直すコンタクト補正、Mixamo FBX／VRM／PMX のヒューマノイドキャラクターへのリターゲティングに対応
- 書き出しは FBX／BVH／VMD（MMD用）のほか、Blender プロジェクト形式も可。Blender へはアドオン経由で再生中のボーンをストリーミングし、モーション全体を Action にベイクできる
- Unreal Engine へは Live Link で UE5 の Manny／Quinn や MetaHuman にストリーミング可能。顔トラッキングで ARKit 形式の表情係数も書き出せる
- 導入は git clone → install.cmd → RGBMoCap.cmd。モデルファイルは Model Manager から別途用意する（一部は登録・手動ダウンロードが必要）

リポジトリは 2026-10-26 作成で、2026-11-24 時点でスター約3,200、フォーク約430（GitHub ページで確認）。

## 学び・所感

- 専用スーツやマーカーなしで、手持ちの動画から 3D アニメーション素材を作れるのが要点。Blender／Unreal へのストリーミングまで含むので、ゲームや映像のモーション下ごしらえに使える
- モデルごとに得意不得意があり（README では PromptHMR は複数人の相対配置に強いが全体の質は ExMR が上、など）使い分け前提の設計。導入手順を AI エージェントに任せるための AGENTS.md／ガイドが同梱されているのも今風
