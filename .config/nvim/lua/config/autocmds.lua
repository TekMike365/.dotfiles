-- Define autocommands with Lua APIs
-- See: h:api-autocmd, h:augroup
local augroup = vim.api.nvim_create_augroup -- Create/get autocommand group
local autocmd = vim.api.nvim_create_autocmd -- Create autocommand

-- General settings

-- Highlight on yank
autocmd("TextYankPost", {
  callback = function()
    vim.highlight.on_yank({
      higroup = "IncSearch",
      timeout = "1000"
    })
  end
})

-- Remove whitespace on save
autocmd("BufWritePre", {
  pattern = "",
  command = ":%s/\\s\\+$//e"
})

-- Don"t auto commenting new lines
autocmd("BufEnter", {
  pattern = "",
  command = "set fo-=c fo-=r fo-=o"
})

-- Set tab to 2
autocmd("Filetype", {
  pattern = {"xml", "html", "xhtml", "css", "scss", "javascript", "typescript", "yaml", "lua"},
  command = "setlocal shiftwidth=2 tabstop=2"
})

-- Disable expand
autocmd("Filetype", {
  pattern = {"make"},
  command = "setlocal expandtab=true shiftwidth=8 softtabstop=0"
})

-- spellcheck or smthn
autocmd("Filetype", {
  pattern = {"gitcommit", "markdown", "text"},
  callback = function()
    vim.opt_local.wrap = true
    vim.opt_local.spell = true
  end
})
