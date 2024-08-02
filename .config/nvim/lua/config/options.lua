-- Options are automatically loaded before lazy.nvim startup
-- Default options that are alearays set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

-- indention
local indent = 4
vim.opt.autoindent = true -- auto indentation
vim.opt.expandtab = true -- convert tabs to spaces
vim.opt.shiftwidth = indent -- the number of spaces inserted for each indentation
vim.opt.smartindent = true -- make indenting smarter
vim.opt.softtabstop = indent -- when hitting <BS>, pretend like a tab is removed, even if spaces
vim.opt.tabstop = indent -- insert N spaces for a tab
vim.opt.shiftround = true -- use multiple of shiftwidth when indenting with "<" and ">"

vim.opt.scrolloff = 16
