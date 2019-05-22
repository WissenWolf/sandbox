import tkinter
#
# cursors = []
#
# with open('cursors') as f:
#     fout = list(map(str.rstrip, f))
#
#     out = open('cursors.out', 'w')
#     for cursor_name in fout:
#         # with open('cursors.out', 'w+') as out:
#         ret = "'{}',\n".format(cursor_name)
#         out.write(ret)
#     out.close()
# print(fout)

cursors = [
        'X_cursor',
        'arrow',
        'based_arrow_down',
        'based_arrow_up',
        'boat',
        'bogosity',
        'bottom_left_corner',
        'bottom_right_corner',
        'bottom_side',
        'bottom_tee',
        'box_spiral',
        'center_ptr',
        'circle',
        'clock',
        'coffee_mug',
        'cross',
        'cross_reverse',
        'crosshair',
        'diamond_cross',
        'dot',
        'dotbox',
        'double_arrow',
        'draft_large',
        'draft_small',
        'draped_box',
        'exchange',
        'fleur',
        'gobbler',
        'gumby',
        'hand1',
        'hand2',
        'heart',
        'icon',
        'iron_cross',
        'left_ptr',
        'left_side',
        'left_tee',
        'leftbutton',
        'll_angle',
        'lr_angle',
        'man',
        'middlebutton',
        'mouse',
        'none',
        'pencil',
        'pirate',
        'plus',
        'question_arrow',
        'right_ptr',
        'right_side',
        'right_tee',
        'rightbutton',
        'rtl_logo',
        'sailboat',
        'sb_down_arrow',
        'sb_h_double_arrow',
        'sb_left_arrow',
        'sb_right_arrow',
        'sb_up_arrow',
        'sb_v_double_arrow',
        'shuttle',
        'sizing',
        'spider',
        'spraycan',
        'star',
        'target',
        'tcross',
        'top_left_arrow',
        'top_left_corner',
        'top_right_corner',
        'top_side',
        'top_tee',
        'trek',
        'ul_angle',
        'umbrella',
        'ur_angle',
        'watch',
        'xterm',
        ]
root = tkinter.Tk()
print(cursors.__len__())

x = 0
y = 0
for n,cursor in enumerate(cursors):
    # print("x = {}, y = {}, cursor = {} ".format(x, y, 13+(y-x)))
    # print("n = {}, cursor = {} ".format(n, cursor))
    # x = n%6
    y = n%13
    if y%13 == 0:
        x += 1
    # print("x = {}, y = {} ".format(x, y))
    label = tkinter.Label(root, text="{}".format(cursor), cursor="{} red".format(cursor), border=1, height=2, width=16, relief=tkinter.RIDGE)
    label.grid(row=x, column=y)

# for x in range(0,6):
#     for y in range(0,13):
        # if cursors[x+y]:
        #     cursor = cursors[x+y]
        #     print("x = {}, y = {}, cursor = {} name = {}".format(x, y, x+y, cursor))

root.configure(cursor="dotbox #ff0000")
root.mainloop()