from PIL import Image, ImageEnhance, ImageFilter
import os

class imageEditor():
    def __init__(self):
        self.enhancedImage = None
        self.prevImage = []
        self.imageFile = None
        self.image = None
        self.dirPath = None

    def setImageFile(self, imageFile):
        self.dirPath = os.path.dirname(imageFile)
        self.imageFile = os.path.basename(imageFile)
        self.image = Image.open(imageFile)
        self.enhancedImage = self.image
        self.prevImage = []
        self.prevImage.append(self.image)

    def store(self):
        self.prevImage.append(self.enhancedImage)

    def restore(self):
        self.enhancedImage = self.prevImage.pop()

    def reset(self):
        self.enhancedImage = self.image

    def autoEnhance(self):
        self.store()
        self.enhancedImage = self.enhancedImage.filter(ImageFilter.SHARPEN)

    def editSharpness(self, enfactor):
        self.store()
        imgEnhancer = ImageEnhance.Sharpness(self.enhancedImage)
        self.enhancedImage = imgEnhancer.enhance(enfactor)

    def editContrast(self, enfactor):
        self.store()
        imgEnhancer = ImageEnhance.Contrast(self.enhancedImage)
        self.enhancedImage = imgEnhancer.enhance(enfactor)

    def editBrightness(self, enfactor):
        self.store()
        imgEnhancer = ImageEnhance.Brightness(self.enhancedImage)
        self.enhancedImage = imgEnhancer.enhance(enfactor)

    def saveImage(self, dirPath):
        self.enhancedImage.save(os.path.join(dirPath, self.imageFile))

    def getImage(self):
        return self.enhancedImage

    def getImageSize(self, baseSize):
        imgWidth, imgHeight = self.image.size

        factor = 1
        if imgWidth > baseSize[0] or imgHeight > baseSize[1]:
            if imgHeight / baseSize[1] > imgWidth / baseSize[0]:
                factor = imgHeight / baseSize[1]
            else:
                factor = imgWidth / baseSize[0]

        imgWidth /= factor
        imgHeight /= factor
        return imgWidth, imgHeight

if __name__ == "__main__":
    path = './resources/'
    editedPath = './edited/'

    for filename in os.listdir(path):
        img = Image.open(path + filename)

        edit = img.filter(ImageFilter.SHARPEN) #.convert('L').rotate(-90)

        factor = 1.2
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(1.1)
        enhancer = ImageEnhance.Sharpness(edit)
        edit = enhancer.enhance(factor)

        brighten = ImageEnhance.Brightness(edit)
        edit = brighten.enhance(1.1)

        edit.save(editedPath + filename)
