# -*- coding: UTF-8 -*-

class Swope_Operation:

    def getSize(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return x, y

        # 向左滑动

    def swipeLeft(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        driver.swipe(x1, y1, x2, y1, t)

        # 向右滑动

    def swipeRight(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        driver.swipe(x1, y1, x2, y1, t)

        # 向上滑动

    def swipeUp(self, driver,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        driver.swipe(x1, y1, x1, y2, t)

        # 向下滑动

    def swipeDown(self, driver, t):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        driver.swipe(x1, y1, x1, y2, t)