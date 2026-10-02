import FreeSimpleGUI as gui;

def get_layout():
	panelSize = (300, 130);

	# 概要&ブラウザパネル
	browseColumn = gui.Column([
		[gui.Text("画像の平行移動と反転を実行できます。\n問題が起こっても責任取れないので注意してください。", size=(50, 3))],
		[
			gui.Text("ファイル（複数選択可）"), gui.InputText(size=(25, 5), key="-FELES-"),
			gui.FilesBrowse(key="-BROWSE-", target="-FELES-", file_types=(("Image", "*.png;*.jpg;*.jpeg;*.bmp;*.webp;*.gif"),))
		],
	], justification="c");

	# 平行移動パネル
	shiftFrame = gui.Frame("平行移動", [
		# [gui.Text("選択した画像を上下左右に平行移動させます。", size=(50, 1))],
		# [gui.HorizontalSeparator(color="gray")],
		[gui.Text("X方向移動量（右方向が正）"), gui.InputText(size=(10, 1), key="-OFFSET_X-", default_text="0")],
		[gui.Text("Y方向移動量（下方向が正）"), gui.InputText(size=(10, 1), key="-OFFSET_Y-", default_text="0")],
		[gui.Button("処理開始", key="-SHIFT_START-")]
	], size=panelSize);

	# 反転パネル
	flipFrame = gui.Frame("反転", [
		[gui.Checkbox("左右反転", key="-FLIP_Y_AXIS-", default=True)],
		[gui.Checkbox("上下反転", key="-FLIP_X_AXIS-")],
		[gui.Button("処理開始", key="-FLIP_START-")]
	], size=panelSize);

	# 全体レイアウト
	layout = [
		[browseColumn],
		[shiftFrame, flipFrame]
	];
	return layout;