"""
Class NMS
Non-Maximum Supression simple implemetation.
@author: tomn681 (Tomás de la Sotta K.)
"""
class NMS:

    """
    Base constructor.
    Class stores box_set and a defined threshold.
    """
    def __init__(box_set, threshold):
        self.box_set = box_set
        self.threshold = threshold

    """
    Simple box_set list value getter
    """
    def get_box_set():
        return self.box_set

    """
    intersection_area
    Computes the area formed between two rectangular boxes.
    Box defined as (x, y, w, h), with (x, y) top-left corner of bounding box
    and w, h, width and height respectively.
    """
    def intersection_area(self, bbox1, bbox2):
        try:
            x1, y1, w1, h1 = bbox1
            x2, y2, w2, h2 = bbox2
            delta_x = min(x1 + w1, x2 + w2) - max(x1, x2)
            delta_y = min(y1, y2) - max(y1 - h1, y2 - h2)
            return delta_x * delta_y
        except:
            raise Exception("Input should be list-type objects as (x, y, w, h), being (x, y) the top left corner.")

    """
    union_area
    Computes the area formed by the union of two rectangular boxes.
    Box defined as (x, y, w, h), with (x, y) top-left corner of bounding box
    and w, h, width and height respectively.
    """
    def union_area(self, bbox1, bbox2):
        try:
            x1, y1, w1, h1 = bbox1
            x2, y2, w2, h2 = bbox2
            area1 = w1 * h1
            area2 = w2 * h2
            return area1 + area2 - self.intersection_area(bbox1, bbox2)
        except:
            raise Exception("Input should be list-type objects as (x, y, w, h), being (x, y) the top left corner.")

    """
    IOU
    Computes the IOU between two given bounding boxes.
    Box defined as (x, y, w, h), with (x, y) top-left corner of bounding box
    and w, h, width and height respectively.
    """
    def IOU(self, bbox1, bbox2):
        return 1.0 * self.union_area(bbox1, bbox2)/self.intersection_area(bbox1, bbox2)

    """
    nms
    Applies the Non-Maximum Supression algorithm to the stored bbox set.
    """
    def nms(self):
        cleaned_box_set = []
        for box in self.get_box_set:
            self.box_set.remove(box)
            keep = True
            for other_box in self.get_box_set:
                if self.IOU(box, other_box) > self.threshold:
                    keep = False
            if keep:
                cleaned_box_set.append(box)
        self.box_set = clean_box_set
