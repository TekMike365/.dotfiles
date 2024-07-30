if vim.fn.has('nvim-0.8') == 0 then
  error('Need Neovim 0.8+ in order to use this config')
end

local required_programs = {"git", "rg"}
for _, cmd in ipairs(required_programs) do
  local name = type(cmd) == "string" and cmd or vim.inspect(cmd)
  local commands = type(cmd) == "string" and {cmd} or cmd
  ---@cast commands string[]
  local found = false

  for _, c in ipairs(commands) do
    if vim.fn.executable(c) == 1 then
      name = c
      found = true
    end
  end

  if not found then
    error(("`%s` is not installed"):format(name))
  end
end

require("config")