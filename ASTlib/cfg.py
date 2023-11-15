from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('quick sort', 'file.py')
cfg.build_visual('qsort', 'png')