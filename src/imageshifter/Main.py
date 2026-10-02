import FreeSimpleGUI as gui;
import os;
import sys;
import Layout
import ImageProcessor;

# uv run pyinstaller .\Main.spec 

# 1ファイルにまとめると起動が遅くなる
# あえてそうする理由はないか

# pyinstallerでまとめた画像ファイル等は実行時に展開される
# ただし、展開先はカレントディレクトリではなく専用のディレクトリだ
# そちらを使う場合（exe化した後など）は、そっちから読み込んでくるようにパスを修正する
# 1ファイル化していないケースでも効いた
def resource_path(relativePass):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relativePass);
    return os.path.join(os.path.abspath('.'), relativePass);

# floatへの変換を試して数値かどうかを判定
def is_float(str):
	try:
		float(str);
	except:
		return False;
	return True;

# 準備
gui.theme("SystemDefault1");
window = gui.Window("イメージシフター", Layout.get_layout(), icon=resource_path("ImageShifter_256.ico"));

# メインループ
while True:
	event, values = window.read();

	# 終了
	if event == gui.WIN_CLOSED or event == "-EXIT-":
		break;

	# 反転
	if event == "-FLIP_START-":
		files = values["-FELES-"].split(";");
		print(files);

		if (files == [] or files == [""]):
			gui.popup_ok("画像が見つかりませんでした", title="Info");
			continue;

		result = gui.popup_ok_cancel("処理を開始してもよろしいですか？", title="Info");
		if result == "OK":
			ImageProcessor.flip_images(files, values["-FLIP_X_AXIS-"], values["-FLIP_Y_AXIS-"]);
			gui.popup_ok("完了しました。", title="Info");

	# シフト
	if event == "-SHIFT_START-":
		files = values["-FELES-"].split(";");
		print(files);

		if (files == [] or files == [""]):
			gui.popup_ok("画像が見つかりませんでした", title="Info");
			continue;

		if not is_float(values["-OFFSET_X-"]) or not is_float(values["-OFFSET_Y-"]):
			gui.popup_ok("オフセットは数値入力です", title="Info");
			continue;

		result = gui.popup_ok_cancel("処理を開始してもよろしいですか？", title="Info");
		if result == "OK":
			ImageProcessor.shift_images(files, values["-OFFSET_X-"], values["-OFFSET_Y-"]);
			gui.popup_ok("完了しました。", title="Info");

window.close();
