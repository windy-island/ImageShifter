import cv2;
import numpy as np;
import os;

# cv2は日本語ファイルやパスを扱えないため、numpy経由で開く
def load_img(path):
	buf = np.fromfile(path, np.uint8);
	img = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED);
	return img;

# 書き込みもロード同様に
def write_img(filePath, image, ext):
	ret, buf = cv2.imencode(ext, image);
	with open(filePath, mode="w+b") as f:
		buf.tofile(f);

# 画像ファイルかチェック
IMG_EXT_LIST = [".png", ".bmp", ".jpg", ".jpeg", ".webp", ".gif"];
def check_image(path):
	ext = os.path.splitext(path)[1];
	for IMG_EXT in IMG_EXT_LIST:
		if ext == IMG_EXT:
			return True;
	return False;

# 画像を反転させる
# XY軸それぞれに対して反転させるかどうかを指定
def flip_images(imgPathList, xAxisFlag, yAxisFlag):

	print(f"xAxisFlag: {xAxisFlag}");
	print(f"yAxisFlag: {yAxisFlag}");

	flipCode = 1;
	if xAxisFlag == True and yAxisFlag == True:		# 上下左右反転
		flipCode = -1;
	elif xAxisFlag == True and yAxisFlag == False:	# 上下反転
		flipCode = 0;
	elif xAxisFlag == False and yAxisFlag == True:	# 左右反転
		flipCode = 1;
	else:											# 反転なし
		return;
	print(f"flipCode: {flipCode}");

	# ファイルを走査して反転
	for path in imgPathList:
		if (not check_image(path)):
			print("not image!");
			continue;
		ext = os.path.splitext(path)[1];
		img = load_img(path);						# ロード
		imgFlipped = cv2.flip(img, flipCode);		# 反転
		write_img(path, imgFlipped, ext);			# 保存
		print(f"finished: {path}");
	return;

# 画像をシフトする
def shift_images(imgPathList, offsetX, offsetY):

	matrix = np.float32([
		[1, 0, offsetX],
		[0, 1, offsetY]
	]);

	# ファイルを走査してシフト
	for path in imgPathList:
		if (not check_image(path)):
			print("not image!");
			continue;
		ext = os.path.splitext(path)[1];
		img = load_img(path);										# ロード
		h, w = img.shape[:2];
		imgShifted = cv2.warpAffine(img, matrix, (int(w), int(h)));	# シフト
		write_img(path, imgShifted, ext);							# 保存
		print(f"finished: {path}");
	return;