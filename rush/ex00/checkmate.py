#!/usr/bin/env python3
import numpy as np

""" checkmate.py """

def checkmate(board):
    """ checkmate.py """
    try:
        # Parse board
        data = [i for i in board.replace('\n', '')]
        data = np.array(data)
        n = int(np.sqrt(len(data)))
        
        # Check if board is square
        if len(data) != n * n:
            print("Fail")
            return
            
        data = data.reshape(n, n)
        
        # Find King position
        king_pos = np.argwhere(data == 'K')
        if len(king_pos) != 1:
            print("Fail")
            return
        
        king_pos = king_pos[0]
        
        # Create attack map
        attack_map = np.zeros((n, n), dtype=bool)
        
        # P Range (Pawn attacks)
        all_p_pos = np.argwhere(data == 'P')
        for p_pos in all_p_pos:
            # Pawns attack diagonally forward (up the board)
            if p_pos[0] != 0:  # Not on top edge
                if p_pos[1] != 0:  # Not on left edge
                    attack_map[p_pos[0]-1, p_pos[1]-1] = True
                if p_pos[1] != n-1:  # Not on right edge
                    attack_map[p_pos[0]-1, p_pos[1]+1] = True
                
        # R Range (Rook attacks)
        all_r_pos = np.argwhere(data == 'R')
        for r_pos in all_r_pos:
            i = 1
            up_con = True
            down_con = True
            lf_con = True
            rt_con = True
            
            while up_con or down_con or lf_con or rt_con:
                # Up
                if up_con:
                    if r_pos[0]-i < 0:
                        up_con = False
                    elif data[r_pos[0]-i, r_pos[1]] != '.':
                        attack_map[r_pos[0]-i, r_pos[1]] = True
                        up_con = False
                    else:
                        attack_map[r_pos[0]-i, r_pos[1]] = True

                # Down
                if down_con:
                    if r_pos[0]+i > n-1:
                        down_con = False
                    elif data[r_pos[0]+i, r_pos[1]] != '.':
                        attack_map[r_pos[0]+i, r_pos[1]] = True
                        down_con = False
                    else:
                        attack_map[r_pos[0]+i, r_pos[1]] = True
            
                # Left
                if lf_con:
                    if r_pos[1]-i < 0:
                        lf_con = False
                    elif data[r_pos[0], r_pos[1]-i] != '.':
                        attack_map[r_pos[0], r_pos[1]-i] = True
                        lf_con = False
                    else:
                        attack_map[r_pos[0], r_pos[1]-i] = True
            
                # Right
                if rt_con:
                    if r_pos[1]+i > n-1:
                        rt_con = False
                    elif data[r_pos[0], r_pos[1]+i] != '.':
                        attack_map[r_pos[0], r_pos[1]+i] = True
                        rt_con = False
                    else:
                        attack_map[r_pos[0], r_pos[1]+i] = True

                i += 1
        
        # B Range (Bishop attacks)
        all_b_pos = np.argwhere(data == 'B')
        for b_pos in all_b_pos:
            i = 1
            pp_con = True  # ++
            nn_con = True  # --
            pn_con = True  # +-
            np_con = True  # -+
            
            while pp_con or nn_con or pn_con or np_con:
                # ++
                if pp_con:
                    if b_pos[0]+i > n-1 or b_pos[1]+i > n-1:
                        pp_con = False
                    elif data[b_pos[0]+i, b_pos[1]+i] != '.':
                        attack_map[b_pos[0]+i, b_pos[1]+i] = True
                        pp_con = False
                    else:
                        attack_map[b_pos[0]+i, b_pos[1]+i] = True

                # --
                if nn_con:
                    if b_pos[0]-i < 0 or b_pos[1]-i < 0:
                        nn_con = False
                    elif data[b_pos[0]-i, b_pos[1]-i] != '.':
                        attack_map[b_pos[0]-i, b_pos[1]-i] = True
                        nn_con = False
                    else:
                        attack_map[b_pos[0]-i, b_pos[1]-i] = True
            
                # +-
                if pn_con:
                    if b_pos[0]+i > n-1 or b_pos[1]-i < 0:
                        pn_con = False
                    elif data[b_pos[0]+i, b_pos[1]-i] != '.':
                        attack_map[b_pos[0]+i, b_pos[1]-i] = True
                        pn_con = False
                    else:
                        attack_map[b_pos[0]+i, b_pos[1]-i] = True
            
                # -+
                if np_con:
                    if b_pos[0]-i < 0 or b_pos[1]+i > n-1:
                        np_con = False
                    elif data[b_pos[0]-i, b_pos[1]+i] != '.':
                        attack_map[b_pos[0]-i, b_pos[1]+i] = True
                        np_con = False
                    else:
                        attack_map[b_pos[0]-i, b_pos[1]+i] = True

                i += 1
        
        # Q Range (Queen attacks - combines Rook and Bishop)
        all_q_pos = np.argwhere(data == 'Q')
        for q_pos in all_q_pos:
            # Rook-like movement
            i = 1
            up_con = True
            down_con = True
            lf_con = True
            rt_con = True
            
            while up_con or down_con or lf_con or rt_con:
                # Up
                if up_con:
                    if q_pos[0]-i < 0:
                        up_con = False
                    elif data[q_pos[0]-i, q_pos[1]] != '.':
                        attack_map[q_pos[0]-i, q_pos[1]] = True
                        up_con = False
                    else:
                        attack_map[q_pos[0]-i, q_pos[1]] = True

                # Down
                if down_con:
                    if q_pos[0]+i > n-1:
                        down_con = False
                    elif data[q_pos[0]+i, q_pos[1]] != '.':
                        attack_map[q_pos[0]+i, q_pos[1]] = True
                        down_con = False
                    else:
                        attack_map[q_pos[0]+i, q_pos[1]] = True
            
                # Left
                if lf_con:
                    if q_pos[1]-i < 0:
                        lf_con = False
                    elif data[q_pos[0], q_pos[1]-i] != '.':
                        attack_map[q_pos[0], q_pos[1]-i] = True
                        lf_con = False
                    else:
                        attack_map[q_pos[0], q_pos[1]-i] = True
            
                # Right
                if rt_con:
                    if q_pos[1]+i > n-1:
                        rt_con = False
                    elif data[q_pos[0], q_pos[1]+i] != '.':
                        attack_map[q_pos[0], q_pos[1]+i] = True
                        rt_con = False
                    else:
                        attack_map[q_pos[0], q_pos[1]+i] = True

                i += 1
            
            # Bishop-like movement
            i = 1
            pp_con = True
            nn_con = True
            pn_con = True
            np_con = True
            
            while pp_con or nn_con or pn_con or np_con:
                # ++
                if pp_con:
                    if q_pos[0]+i > n-1 or q_pos[1]+i > n-1:
                        pp_con = False
                    elif data[q_pos[0]+i, q_pos[1]+i] != '.':
                        attack_map[q_pos[0]+i, q_pos[1]+i] = True
                        pp_con = False
                    else:
                        attack_map[q_pos[0]+i, q_pos[1]+i] = True

                # --
                if nn_con:
                    if q_pos[0]-i < 0 or q_pos[1]-i < 0:
                        nn_con = False
                    elif data[q_pos[0]-i, q_pos[1]-i] != '.':
                        attack_map[q_pos[0]-i, q_pos[1]-i] = True
                        nn_con = False
                    else:
                        attack_map[q_pos[0]-i, q_pos[1]-i] = True
            
                # +-
                if pn_con:
                    if q_pos[0]+i > n-1 or q_pos[1]-i < 0:
                        pn_con = False
                    elif data[q_pos[0]+i, q_pos[1]-i] != '.':
                        attack_map[q_pos[0]+i, q_pos[1]-i] = True
                        pn_con = False
                    else:
                        attack_map[q_pos[0]+i, q_pos[1]-i] = True
            
                # -+
                if np_con:
                    if q_pos[0]-i < 0 or q_pos[1]+i > n-1:
                        np_con = False
                    elif data[q_pos[0]-i, q_pos[1]+i] != '.':
                        attack_map[q_pos[0]-i, q_pos[1]+i] = True
                        np_con = False
                    else:
                        attack_map[q_pos[0]-i, q_pos[1]+i] = True

                i += 1
        
        # Check if King is in check
        if attack_map[king_pos[0], king_pos[1]]:
            print("Success")
        else:
            print("Fail")
            
    except (ValueError, IndexError):
        print("Fail")
