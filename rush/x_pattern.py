#!/usr/bin/env python3
import numpy as np

""" checkmate.py """

def checkmate(board):
    """ checkmate.py """
    pass

if __name__ == "__main__":
    board = """\
.....
.K...
..RP.
P....
P...P\
"""
    try :
        #print(board)
        data = [i for i in board.replace('\n', '')]
        data = np.array(data)
        n = int(np.sqrt(len(data)))
        data = data.reshape(n, n)
        print(data)
        print(data.shape)
        
        #Unit Position
        #print(np.argwhere(data == 'P'))
        #print(np.argwhere(data == 'B'))
        #print(np.argwhere(data == 'R'))
        #print(np.argwhere(data == 'Q'))
        
        #print(np.argwhere(data == 'K'))
        
        #P Range
        all_p_pos = np.argwhere(data == 'P')
        #print(all_p_pos)

        for p_pos in all_p_pos:
            if p_pos[0] != 0 and p_pos[1] != 0 and p_pos[1] != n - 1:
                data[p_pos[0]-1, p_pos[1]+1] = 'X'
                data[p_pos[0]-1, p_pos[1]-1] = 'X'
            elif p_pos[0] != 0 and p_pos[1] == 0:
                data[p_pos[0]-1, p_pos[1]+1] = 'X'
            elif p_pos[0] != 0 and p_pos[1] == n-1:
                data[p_pos[0]-1, p_pos[1]-1] = 'X'
                
        #R Range
        all_r_pos = np.argwhere(data == 'R')
        #print(all_r_pos)

        #for r_pos in all_r_pos:
            #data[r_pos[0], :] = 'X'  # Horizontal line
            #data[:, r_pos[1]] = 'X'  # Vertical line
        for r_pos in all_r_pos:
            i = 1
            up_con = True
            down_con = True
            lf_con = True
            rt_con = True
            while up_con+down_con+lf_con+rt_con:
                #up
                if r_pos[0]-i < 0:
                    up_con = False
                elif data[r_pos[0]-i, r_pos[1]] != '.':
                    up_con = False
                if up_con:
                    data[r_pos[0]-i, r_pos[1]] = 'X'

                #down
                if r_pos[0]+i > n-1:
                    down_con = False
                elif data[r_pos[0]+i, r_pos[1]] != '.':
                    down_con = False
                if down_con:
                    data[r_pos[0]+i, r_pos[1]] = 'X'
            
                #left
                if r_pos[1]-i < 0:
                    lf_con = False
                elif data[r_pos[0], r_pos[1]-i] != '.':
                    lf_con = False
                if lf_con:
                    data[r_pos[0], r_pos[1]-i] = 'X'
            
                #right
                if r_pos[1]+i > n-1:
                    rt_con = False
                elif data[r_pos[0], r_pos[1]+i] != '.':
                    rt_con = False
                if rt_con:
                    data[r_pos[0], r_pos[1]+i] = 'X'

                i += 1
        
        
        #B Range
        all_b_pos = np.argwhere(data == 'B')
        #print(all_b_pos)

        for b_pos in all_b_pos:
            i = 1
            pp_con = True
            nn_con = True
            pn_con = True
            np_con = True
            while pp_con+nn_con+pn_con+np_con:
                #++
                if b_pos[0]+i > n-1 or b_pos[1]+i > n-1:
                    pp_con = False
                else:
                    data[b_pos[0]+i, b_pos[1]+i] = 'X'

                #--
                if b_pos[0]-i < 0 or b_pos[1]-i < 0:
                    nn_con = False
                else:
                    data[b_pos[0]-i, b_pos[1]-i] = 'X'
            
                #+-
                if b_pos[0]+i > n-1 or b_pos[1]-i < 0:
                    pn_con = False
                else:
                    data[b_pos[0]+i, b_pos[1]-i] = 'X'
            
                #-+
                if b_pos[0]-i < 0 or b_pos[1]+i > n-1:
                    np_con = False
                else:
                    data[b_pos[0]-i, b_pos[1]+i] = 'X'

                i += 1
            
        #Check Range
        print('Check Range:', data, sep='\n')
        
    except ValueError:
        print("Wrong Dimension")